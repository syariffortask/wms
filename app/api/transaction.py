from fastapi import APIRouter
from fastapi import Depends
from sqlmodel import Session
from app.core.database import get_session
from app.schemas.transaction import TransactionCreate,TransactionDetailRead
from app.controller.transaction_controller import get_transactions_controller
from app.controller.transaction_controller import get_transaction_controller
from app.controller.transaction_controller import create_transaction_controller

router = APIRouter(
    prefix="/transactions",
    tags=["transactions"],
    responses={404: {"description": "Not found"}},
)

@router.get("/")
def read_transactions(session: Session = Depends(get_session)):
    return get_transactions_controller(session)

@router.post("/",response_model=TransactionDetailRead)
def create_transaction(data: TransactionCreate, session: Session = Depends(get_session)):
    return create_transaction_controller(session, data)


@router.get("/{trx_id}",response_model=TransactionDetailRead)
def read_transaction(trx_id: int, session: Session = Depends(get_session)):
    return get_transaction_controller(session, trx_id)