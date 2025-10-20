import typer
from app.core.database import create_db_and_tables, drop_db_and_tables, get_session
from app.core.security import hash_password
from app.models import User


app = typer.Typer()

@app.command()
def migrate():
    create_db_and_tables()
    print("✅  Migration completed")
    
@app.command()
def drop():
    drop_db_and_tables()
    print("✅  All tables dropped")
    
@app.command()
def createuser():
    # input prompt
    username = typer.prompt("Username: ")
    password = typer.prompt("Password: ", hide_input=True,confirmation_prompt=True)
    nik = typer.prompt("NIK: ")
    role = typer.prompt("Role: ",default="admin")
    
    session = next(get_session())
    password = hash_password(password)
    user = User(nik=nik,name=username, password=password, role=role, is_active=True)
    session.add(user)
    session.commit()
    print("✅  Superuser created")

    
    
    
if __name__ == "__main__":
    app()