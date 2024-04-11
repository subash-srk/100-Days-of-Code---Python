is_human: bool
name: str


def police_check(age: int) -> bool:
    if age > 18:
        return True
    else:
        return False


if police_check(20):
    print("You can drive")
else:
    print("you cant drive")