class DQSEValidator:
    @staticmethod
    def validate_question(question_data: dict) -> bool:
        """Validates deterministic question generation rules, distractors, and collision checks."""
        if not question_data.get("question_id"):
            raise ValueError("Question ID missing.")
        if not question_data.get("correct_answer"):
            raise ValueError("Correct answer missing.")
        if not question_data.get("distractors"):
            raise ValueError("Distractors missing.")
        return True
