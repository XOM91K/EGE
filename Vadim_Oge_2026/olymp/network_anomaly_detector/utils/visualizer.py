import asyncio
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
from collections import deque
import threading

class RealTimeVisualizer:
    def __init__(self, max_points=1000):
        self.max_points = max_points
        self.anomaly_data = deque(maxlen=max_points)
        self.traffic_data = deque(maxlen=max_points)
        self.app = dash.Dash(__name__)
        self.setup_dashboard()
        
    def setup_dashboard(self):
        """Настройка Dash dashboard"""
        self.app.layout = html.Div([
            html.H1("Network Anomaly Detection Dashboard"),
            
            html.Div([
                dcc.Graph(id='anomaly-graph'),
                dcc.Interval(id='interval', interval=1000)
            ]),
            
            html.Div([
                dcc.Graph(id='traffic-graph'),
            ]),
            
            html.Div([
                html.H3("Recent Anomalies"),
                html.Ul(id='anomaly-list')
            ])
        ])
        
        @self.app.callback(
            [Output('anomaly-graph', 'figure'),
             Output('traffic-graph', 'figure'),
             Output('anomaly-list', 'children')],
            [Input('interval', 'n_intervals')]
        )
        def update_dashboard(n):
            return self._create_figures()
    
    def _create_figures(self):
        """Создание графиков для dashboard"""
        # График аномалий
        anomaly_fig = go.Figure(
            data=[go.Scatter(
                y=list(self.anomaly_data),
                mode='lines+markers',
                name='Anomaly Score'
            )]
        )
        anomaly_fig.update_layout(title='Real-time Anomaly Detection')
        
        # График трафика
        traffic_fig = go.Figure(
            data=[go.Scatter(
                y=list(self.traffic_data),
                mode='lines',
                name='Traffic Volume'
            )]
        )
        traffic_fig.update_layout(title='Network Traffic Volume')
        
        # Список аномалий
        anomaly_list = [
            html.Li(f"Anomaly at point {i}") 
            for i in range(min(10, len(self.anomaly_data)))
        ]
        
        return anomaly_fig, traffic_fig, anomaly_list
    
    def update_data(self, anomaly):
        """Обновление данных для визуализации"""
        score = self._calculate_anomaly_score(anomaly)
        self.anomaly_data.append(score)
        self.traffic_data.append(len(self.anomaly_data))
    
    def _calculate_anomaly_score(self, anomaly):
        """Расчет скора аномалии на основе серьезности"""
        severity_scores = {'LOW': 1, 'MEDIUM': 2, 'HIGH': 3}
        return severity_scores.get(anomaly.get('severity', 'LOW'), 1)
    
    async def start_dashboard(self):
        """Запуск dashboard в отдельном потоке"""
        def run_dashboard():
            self.app.run_server(debug=False, host='0.0.0.0', port=8050)
        
        thread = threading.Thread(target=run_dashboard)
        thread.daemon = True
        thread.start()
    
    def stop(self):
        """Остановка визуализатора"""
        pass