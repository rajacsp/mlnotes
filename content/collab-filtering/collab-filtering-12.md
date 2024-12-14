---
title: Collab-Filtering-12
date: 2024-12-14
author: Your Name
cell_count: 15
score: 15
---

```python

```


```python
# !pip install scikit-learn
```


```python
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.impute import SimpleImputer

# Step 1: Create a dummy dataset
data = {
    "User": ["User1", "User1", "User1", "User2", "User2", "User3", "User3", "User4"],
    "Video": ["Video1", "Video2", "Video3", "Video1", "Video4", "Video2", "Video3", "Video4"],
    "Rating": [5, 3, 4, 4, 5, 2, 3, 4]
}
```


```python
df = pd.DataFrame(data)
print("Original Dataset:")
print(df)

```

    Original Dataset:
        User   Video  Rating
    0  User1  Video1       5
    1  User1  Video2       3
    2  User1  Video3       4
    3  User2  Video1       4
    4  User2  Video4       5
    5  User3  Video2       2
    6  User3  Video3       3
    7  User4  Video4       4



```python
# Step 2: Pivot the dataset to create a user-video matrix
user_video_matrix = df.pivot_table(index='User', columns='Video', values='Rating')
print("\nUser-Video Matrix:")
print(user_video_matrix)
```

    
    User-Video Matrix:
    Video  Video1  Video2  Video3  Video4
    User                                 
    User1     5.0     3.0     4.0     NaN
    User2     4.0     NaN     NaN     5.0
    User3     NaN     2.0     3.0     NaN
    User4     NaN     NaN     NaN     4.0



```python
# Step 3: Fill missing values using the mean of each user
imputer = SimpleImputer(strategy="mean")
user_video_matrix_imputed = imputer.fit_transform(user_video_matrix)
```


```python
# Step 4: Compute the similarity between users
user_similarity = cosine_similarity(user_video_matrix_imputed)
user_similarity_df = pd.DataFrame(user_similarity, index=user_video_matrix.index, columns=user_video_matrix.index)
print("\nUser Similarity Matrix:")
print(user_similarity_df)
```

    
    User Similarity Matrix:
    User      User1     User2     User3     User4
    User                                         
    User1  1.000000  0.989916  0.990937  0.999716
    User2  0.989916  1.000000  0.992551  0.989915
    User3  0.990937  0.992551  1.000000  0.993138
    User4  0.999716  0.989915  0.993138  1.000000



```python
# Step 5: Recommend videos for a specific user (e.g., User1)
def recommend_videos(user, user_video_matrix, user_similarity_df, top_n=2):
    # Get the index of the target user
    user_index = user_video_matrix.index.get_loc(user)
    similar_users = user_similarity_df.iloc[user_index].sort_values(ascending=False).index
    
    # Aggregate ratings from similar users
    recommendations = {}
    for similar_user in similar_users:
        if similar_user == user:
            continue
        for video, rating in user_video_matrix.loc[similar_user].dropna().items():
            if pd.isna(user_video_matrix.loc[user, video]):  # Recommend only unseen videos
                recommendations[video] = recommendations.get(video, 0) + rating
    
    # Sort by highest aggregated score
    sorted_recommendations = sorted(recommendations.items(), key=lambda x: x[1], reverse=True)
    return [video for video, _ in sorted_recommendations[:top_n]]
```


```python
# Recommend videos for User1
recommended_videos = recommend_videos("User1", user_video_matrix, user_similarity_df)
print(f"\nRecommended Videos for User1: {recommended_videos}")
```

    
    Recommended Videos for User1: ['Video4']



```python

```


```python

```


```python

```


```python

```


```python

```


```python

```


---
**Score: 15**