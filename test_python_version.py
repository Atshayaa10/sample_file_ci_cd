# This file uses Python 3.10+ match statement
# Will fail on Python 3.9 or earlier

def process_command(command: str) -> str:
    """
    Process commands using match statement (Python 3.10+)
    This will cause SyntaxError on older Python versions
    """
    match command:
        case "start":
            return "Starting application..."
        case "stop":
            return "Stopping application..."
        case "restart":
            return "Restarting application..."
        case "status":
            return "Checking status..."
        case _:
            return f"Unknown command: {command}"

def calculate_grade(score: int) -> str:
    """
    Another match statement example
    """
    match score:
        case score if score >= 90:
            return "A"
        case score if score >= 80:
            return "B"
        case score if score >= 70:
            return "C"
        case score if score >= 60:
            return "D"
        case _:
            return "F"

if __name__ == "__main__":
    # Test the functions
    print(process_command("start"))
    print(process_command("stop"))
    print(process_command("unknown"))
    
    print(f"Score 95: {calculate_grade(95)}")
    print(f"Score 75: {calculate_grade(75)}")
    print(f"Score 55: {calculate_grade(55)}")
