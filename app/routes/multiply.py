from fastapi import APIRouter, HTTPException

router = APIRouter()

@router.get("/multiply")
def calculate_multiply(num1: float, num2: float):
    return {
        "operation": "multiply",
        "num1": num1,
        "num2": num2,
        "result": num1 * num2
    }