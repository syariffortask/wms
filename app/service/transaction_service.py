from sqlmodel import Session, select
from app.schemas.transaction import TransactionCreate
from app.models import Transaction, TransactionItem, Item
from app.schemas.transaction import TrxType
from typing import Optional, List
import uuid


def get_transactions_service(session: Session) -> List[Transaction]:
    return session.exec(select(Transaction)).all()

def get_transaction_service(session: Session, trx_id: int) -> Optional[Transaction]:
    return session.get(Transaction, trx_id)

def create_transaction_service(session: Session, transaction: TransactionCreate) -> Optional[Transaction]:
    try:
        # 🔹 1. Generate kode transaksi unik
        trx_code = f"TRX-{uuid.uuid4().hex[:8].upper()}"

        # 🔹 2. Buat record transaksi baru
        new_transaction = Transaction(
            trx_code=trx_code,
            trx_type=transaction.trx_type,
            note=transaction.note
        )
        session.add(new_transaction)
        session.flush()  # supaya new_transaction.id terisi

        # 🔹 3. Loop semua item transaksi
        for item_data in transaction.items:
            barang = session.get(Item, item_data.item_id)
            if not barang:
                raise ValueError(f"Item dengan ID {item_data.item_id} tidak ditemukan")

            # Validasi stok kalau transaksi keluar
            if transaction.trx_type == TrxType.OUT:
                if barang.stock < item_data.qty:
                    raise ValueError(f"Stok {barang.name} tidak mencukupi (tersisa {barang.stock})")
                barang.stock -= item_data.qty
            else:
                # Barang masuk
                barang.stock += item_data.qty

            # Tambahkan ke tabel detail transaksi
            new_transaction_item = TransactionItem(
                transaction_id=new_transaction.id,
                item_id=item_data.item_id,
                qty=item_data.qty
            )
            session.add(new_transaction_item)

        # 🔹 4. Commit semua perubahan
        session.commit()
        session.refresh(new_transaction)
        return new_transaction

    except ValueError as ve:
        session.rollback()
        raise ve
    except Exception as e:
        session.rollback()
        raise e
