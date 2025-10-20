from app.service.transaction_service import create_transaction_service
from app.service.transaction_service import get_transactions_service
from app.service.transaction_service import get_transaction_service
from app.schemas.transaction import TransactionCreate
from sqlmodel import Session
from app.models import Transaction
from fastapi import HTTPException
from typing import Optional


def get_transactions_controller(session: Session) -> list[Transaction]:
    try:
        transactions = get_transactions_service(session)
        return transactions
    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

def get_transaction_controller(session: Session, trx_id: int) -> Optional[Transaction]:
    try:
        transaction = get_transaction_service(session, trx_id)
        return transaction
    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

def create_transaction_controller(session: Session, transaction: TransactionCreate) -> Transaction:
    try:
        new_transaction = create_transaction_service(session, transaction)
        return new_transaction
    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))