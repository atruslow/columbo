import columbo


def user_has_dog(answers: columbo.Answers) -> bool:
    return answers["has_dog"]


interactions = [
    columbo.Confirm("has_dog", "Do you have a dog?", default=True),
    columbo.BasicQuestion(
        "dog_name",
        "What is the name of the dog?",
        should_ask=user_has_dog,
        default="Kaylee",
    ),
    columbo.BasicQuestion(
        "dog_breed",
        "What is the breed of the dog?",
        should_ask=user_has_dog,
        default="Basset Hound",
    ),
]

user_answers = columbo.get_answers(interactions)
print(user_answers)
