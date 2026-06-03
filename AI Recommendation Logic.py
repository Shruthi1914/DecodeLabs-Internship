movies = {
    "Inception": ["sci-fi", "thriller", "action"],
    "Interstellar": ["sci-fi", "drama", "adventure"],
    "The Dark Knight": ["action", "crime", "thriller"],
    "Avengers: Endgame": ["action", "superhero", "adventure"],
    "Titanic": ["romance", "drama"],
    "The Notebook": ["romance", "drama"],
    "3 Idiots": ["comedy", "drama", "education"],
    "Dangal": ["sports", "drama", "inspirational"],
    "Zindagi Na Milegi Dobara": ["comedy", "adventure", "drama"],
    "The Conjuring": ["horror", "thriller"]
}
user_input = input("Enter your favorite genres (comma-separated): ").lower()
preferences = [genre.strip() for genre in user_input.split(",")]
recommendations = []
for movie, genres in movies.items():
    score = len(set(preferences) & set(genres))
    if score > 0:
        recommendations.append((movie, score))
recommendations.sort(key=lambda x: x[1], reverse=True)
print("\n🎬 Recommended Movies:\n")
if recommendations:
    for movie, score in recommendations:
        print(f"{movie}  | Match Score: {score}")
else:
    print("No matching movies found.")