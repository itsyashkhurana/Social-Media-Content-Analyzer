<<<<<<< HEAD


def analyze_content(text):
    """Analyze social media content and provide improvement suggestions"""
    # Basic analysis implementation
    word_count = len(text.split())
    char_count = len(text)
    
    suggestions = []
    
    # Basic engagement improvement rules
    if word_count > 280:
        suggestions.append("Content is too long for optimal engagement. Consider shortening to under 280 words.")
    
    if "http" not in text:
        suggestions.append("Adding a relevant link could increase engagement.")
        
    if "!" not in text and "?" not in text:
        suggestions.append("Consider adding questions or exclamations to boost interaction.")
        
    return {
        "word_count": word_count,
        "char_count": char_count,
        "suggestions": suggestions if suggestions else ["Content looks good!"]
=======


def analyze_content(text):
    """Analyze social media content and provide improvement suggestions"""
    # Basic analysis implementation
    word_count = len(text.split())
    char_count = len(text)
    
    suggestions = []
    
    # Basic engagement improvement rules
    if word_count > 280:
        suggestions.append("Content is too long for optimal engagement. Consider shortening to under 280 words.")
    
    if "http" not in text:
        suggestions.append("Adding a relevant link could increase engagement.")
        
    if "!" not in text and "?" not in text:
        suggestions.append("Consider adding questions or exclamations to boost interaction.")
        
    return {
        "word_count": word_count,
        "char_count": char_count,
        "suggestions": suggestions if suggestions else ["Content looks good!"]
>>>>>>> master
    }