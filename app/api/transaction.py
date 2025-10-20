from fastapi import APIRouter
from fastapi import Depends
from sqlmodel import Session
from app.core.database import get_session
from app.schemas.transaction import TransactionCreate,TransactionDetailRead
from app.controller.transaction_controller import get_transactions_controller
from app.controller.transaction_controller import get_transaction_controller
from app.controller.transaction_controller import create_transaction_controller
from app.core.security import get_current_user

router = APIRouter(
    prefix="/transactions",
    tags=["transactions"],
    responses={404: {"description": "Not found"}},
)

@router.get("/",response_model=list[TransactionDetailRead], dependencies=[Depends(get_current_user())])
def read_transactions(session: Session = Depends(get_session)):
    return get_transactions_controller(session)

@router.post("/",response_model=TransactionDetailRead, dependencies=[Depends(get_current_user())])
def create_transaction(data: TransactionCreate, session: Session = Depends(get_session)):
    return create_transaction_controller(session, data)


@router.get("/{trx_id}",response_model=TransactionDetailRead, dependencies=[Depends(get_current_user())])
def read_transaction(trx_id: int, session: Session = Depends(get_session)):
    return get_transaction_controller(session, trx_id)