# Categorical / object columns
        elif pd.api.types.is_categorical_dtype(df[col]) or df[col].dtype == object:
            if df[col].nunique() < 20:
                plt.figure(figsize=(6, 4))
                sns.countplot(x=df[col])
                plt.title(f'Countplot of {col}')
                plt.xticks(rotation=45)
                plt.show()
        
        # Wordcloud for text-like columns
        if df[col].dtype == object:
            avg_len = df[col].dropna().str.len().mean()
            if avg_len and avg_len > 20:
                text_data = " ".join(df[col].dropna().astype(str))
                if text_data.strip():
                    wordcloud = WordCloud(width=800, height=400, background_color="white").generate(text_data)
                    plt.figure(figsize=(8, 4))
                    plt.imshow(wordcloud, interpolation="bilinear")
                    plt.axis("off")
                    plt.title(f'WordCloud of {col}')
                    plt.show()

# Sample DataFrame
df = pd.DataFrame({
    "Age": [22, 25, 30, 28, 40, 35, 22],
    "Gender": ["Male", "Female", "Female", "Male", "Male", "Female", "Male"],
    "Comments": ["Good", "Excellent service", "Bad experience", "Okay", "Loved it", "Could be better", "Nice"]
})

# Run the function
visualize(df)
