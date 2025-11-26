import numpy as np
import asyncio
from sklearn.ensemble import IsolationForest
from sklearn.svm import OneClassSVM
from sklearn.preprocessing import StandardScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Dropout
import joblib
import os

class MLAnalyzer:
    def __init__(self, config):
        self.config = config
        self.scaler = StandardScaler()
        self.models = {}
        self.setup_models()
        
    def setup_models(self):
        """Инициализация ML моделей"""
        # Isolation Forest для обнаружения выбросов
        self.models['isolation_forest'] = IsolationForest(
            n_estimators=100,
            contamination=0.1,
            random_state=42
        )
        
        # One-Class SVM
        self.models['one_class_svm'] = OneClassSVM(
            nu=0.1,
            kernel='rbf',
            gamma=0.1
        )
        
        # LSTM для временных рядов (если нужно)
        self.models['lstm'] = self._build_lstm_model()
    
    def _build_lstm_model(self):
        """Построение LSTM модели для анализа временных последовательностей"""
        model = Sequential([
            LSTM(50, return_sequences=True, input_shape=(10, 7)),
            Dropout(0.2),
            LSTM(50, return_sequences=False),
            Dropout(0.2),
            Dense(25),
            Dense(1, activation='sigmoid')
        ])
        model.compile(optimizer='adam', loss='binary_crossentropy')
        return model
    
    async def detect_anomalies(self, features):
        """Обнаружение аномалий с помощью ML"""
        if len(features) == 0:
            return []
        
        # Масштабирование признаков
        features_scaled = self.scaler.fit_transform(features)
        
        anomalies = []
        
        # Использование нескольких моделей для консенсуса
        if_anomalies = self.models['isolation_forest'].fit_predict(features_scaled)
        svm_anomalies = self.models['one_class_svm'].fit_predict(features_scaled)
        
        # Комбинирование результатов
        for i, (if_pred, svm_pred) in enumerate(zip(if_anomalies, svm_anomalies)):
            if if_pred == -1 and svm_pred == -1:
                anomalies.append({
                    'type': 'ML_ANOMALY',
                    'severity': 'HIGH',
                    'description': 'Consensus anomaly detected by multiple ML models',
                    'features': features[i],
                    'timestamp': datetime.now()
                })
        
        return anomalies
    
    async def retrain_models(self):
        """Переобучение моделей на новых данных"""
        # Здесь должна быть логика сбора новых данных и переобучения
        print("Retraining ML models...")
        
        # Сохранение обновленных моделей
        for name, model in self.models.items():
            if hasattr(model, 'fit'):
                joblib.dump(model, f'models/{name}_model.joblib')