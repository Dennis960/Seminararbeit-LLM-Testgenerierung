def highest_scorers(students_scores):
    if not students_scores:
        return []
    
    sorted_scores = sorted(students_scores, key=lambda x: (-x[1], x[0]))
    highest_score = sorted_scores[0][1]
    
    highest_scorers = [name for name, score in sorted_scores if score == highest_score]
    return sorted(highest_scorers)