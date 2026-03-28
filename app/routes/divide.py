from fastapi import APIRouter, HTTPException

router = APIRouter()

@router.get("/divide")
def calculate_divide(num1: float, num2: float):
    if num2 == 0:
        raise HTTPException(status_code=400, detail="No se puede dividir entre 0")
    
    return {
        "operation": "divide",
        "num1": num1, 
        "num2": num2,
        "result": num1 / num2
    }