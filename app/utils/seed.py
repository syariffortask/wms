from sqlmodel import Session, select
from app.core.database import engine
from app.core.security import hash_password
from app.models import User, Item
from app.models.user import Role


# ------------------------
# Seed Users
# ------------------------
def seed_users():
    with Session(engine) as session:
        # 🔹 1. Definisikan user yang ingin di-seed
        users = [
            User(name="Syarif", nik="S0001", role=Role.admin, password=hash_password("123")),
            User(name="user", nik="S0002", role=Role.user, password=hash_password("123")),
        ]

        # 🔹 2. Ambil semua NIK yang sudah ada di DB
        existing_nik = {u.nik for u in session.exec(select(User.nik)).all()}

        # 🔹 3. Filter hanya user baru
        new_users = [u for u in users if u.nik not in existing_nik]

        # 🔹 4. Simpan ke DB
        if new_users:
            session.add_all(new_users)
            session.commit()
            print(f"✅ {len(new_users)} user(s) berhasil di-seed")
        else:
            print("ℹ️ Semua user sudah ada, skip seeding.")

# ------------------------
# Item Seeders
# ------------------------
def seed_items():
    items = [
        Item(sku="PRD001",name="Almound Dolce Body Lotion",rack="A1"),
        Item(sku="PRD002",name="Almound Dolce Silky",rack="A1"),
        Item(sku="PRD003",name="Floriental Firming",rack="A1"),
        Item(sku="PRD004",name="Poem Prebiotic Bright",rack="A2"),
        Item(sku="PRD005",name="Oats Don't Lie",rack="A2"),
        Item(sku="PRD006",name="Ocha",rack="A2"),
        
    ]

    with Session(engine) as session:
        existing_codes = [i.sku for i in session.exec(select(Item)).all()]
        new_items = [i for i in items if i.sku not in existing_codes]

        if new_items:
            session.add_all(new_items)
            session.commit()
            print(f"✅ {len(new_items)} item seeded.")
        else:
            print("ℹ️ Item sudah ada, skip seeding.")



# ------------------------
# Run All Seeders
# ------------------------
def run_seed():
    seed_users()
    seed_items()
    # seed_products()
    print("🎉 All master data seeded")