"""Functions for organizing and calculating student exam scores."""

def round_scores(student_scores):
    """
    :param student_scores (list[float]): Student exam scores.
    :returns (list[int]): Student scores *rounded* to the nearest integer value."""
    
    return [int(round(num)) for num in student_scores]

def count_failed_students(student_scores):
    """
    :param student_scores (list[int]): Student scores as ints.
    :returns (int): The count of student scores at or below 40."""

    failed = 0
    for score in student_scores:
        if score <= 40: failed += 1
    return failed
    
def above_threshold(student_scores, threshold):
    """
    :param student_scores (list[int]): Integer scores.
    :param threshold (int): The threshold to cross to be the "best" score.
    :returns (list[int]): Integer scores that are at or above the "best" threshold."""

    best_scores = []
    for score in student_scores:
        if score >= threshold: best_scores.append(score)
    return best_scores       

def letter_grades(highest):
    """
    :param highest (int): The value of the highest exam score.
    :returns (list[int]): Lower threshold scores for each D-A letter grade interval."""

    step = (highest - 40)//4
    return [41, 41 + step, 41 + (step * 2), 41 + (step * 3)]

def student_ranking(student_scores, student_names):
    """
    :param student_scores (list): Scores in descending order.
    :param student_names (list[str]): Student names by exam score in descending order.
    :returns (list[str]): Strings in format ["<rank>. <student name>: <score>"]."""

    name_with_score = []
    index_pair = 0
    for student in student_names:
        students = f"{index_pair + 1}. {student}: {student_scores[index_pair]}"
        name_with_score.append(students)
        index_pair += 1
    return name_with_score
    
def perfect_score(student_info):
    """
    :param student_info (list[list[str, int]]): List of [<student name>, <score>] lists.
    :returns (list): First `[<student name>, 100]` found OR `[]` if no student score of 100 is found."""

    for student, score in student_info:
        if score == 100:
            return [student, 100] 
    return []