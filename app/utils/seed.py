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
            User(name="Syarif", nik="s0001", role=Role.admin, password=hash_password("123")),
            User(name="user", nik="s0002", role=Role.user, password=hash_password("123")),
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
        Item(sku="PRD7K2A", name="Almond Dolce Body Lotion", rack="A1"),
        Item(sku="PRD9M8B", name="Almond Dolce Silky Lotion", rack="A1"),
        Item(sku="PRD4X5Q", name="Floriental Firming Lotion", rack="A1"),
        Item(sku="PRD1H9T", name="Poem Prebiotic Bright Lotion", rack="A2"),
        Item(sku="PRD3P2F", name="Oats Don't Lie Body Wash", rack="A2"),
        Item(sku="PRD6C4Z", name="Ocha Refreshing Soap", rack="A2"),
        Item(sku="PRD8S7L", name="Lavender Dream Hand Soap", rack="A3"),
        Item(sku="PRD2R9N", name="Coconut Bliss Body Lotion", rack="A3"),
        Item(sku="PRD5T1G", name="Charcoal Detox Face Wash", rack="A3"),
        Item(sku="PRD9B6D", name="Rose Essence Body Scrub", rack="A4"),
        Item(sku="PRD7F3V", name="Green Tea Gentle Cleanser", rack="A4"),
        Item(sku="PRD2N8H", name="Shea Smooth Body Butter", rack="A4"),
        Item(sku="PRD6J5Q", name="Honey Glow Hand Cream", rack="B1"),
        Item(sku="PRD1Z4E", name="Milk & Oat Moisturizer", rack="B1"),
        Item(sku="PRD5W7P", name="Aloe Vera Cooling Gel", rack="B1"),
        Item(sku="PRD8C2R", name="Vanilla Comfort Lotion", rack="B2"),
        Item(sku="PRD3G6M", name="Lemon Fresh Antibac Soap", rack="B2"),
        Item(sku="PRD9K4A", name="Eucalyptus Revive Wash", rack="B2"),
        Item(sku="PRD4P1Y", name="Chamomile Calm Lotion", rack="B3"),
        Item(sku="PRD2T9S", name="Peppermint Energy Soap", rack="B3"),
        Item(sku="PRD6V3B", name="Cocoa Butter Smooth Lotion", rack="B3"),
        Item(sku="PRD1L8X", name="Jasmine Soft Touch Soap", rack="B4"),
        Item(sku="PRD7Q5J", name="Tea Tree Purify Wash", rack="B4"),
        Item(sku="PRD9N2C", name="Olive Restore Lotion", rack="B4"),
        Item(sku="PRD3F6K", name="Ocean Breeze Bath Gel", rack="C1"),
        Item(sku="PRD8W4Z", name="Sakura Blossom Lotion", rack="C1"),
        Item(sku="PRD2M9R", name="Minty Fresh Face Soap", rack="C1"),
        Item(sku="PRD6A3T", name="Cucumber Calm Wash", rack="C2"),
        Item(sku="PRD9Y7E", name="Rosemary Relax Lotion", rack="C2"),
        Item(sku="PRD4C1U", name="Citrus Burst Shower Gel", rack="C2"),
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