from transformers import pipeline

# センチメント分析パイプラインの初期化
nlp = pipeline("sentiment-analysis")

# 分析したいテキスト
text = "I support you."
text_negative = "Disappear!."

# センチメント分析の実行
result = nlp(text)
result_negative = nlp(text_negative)

# 結果の表示
print(f"ポジティブなテキストのセンチメント: {result}")
print(f"ネガティブなテキストのセンチメント: {result_negative}")
