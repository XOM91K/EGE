import requests

def get_ans():
    def get_task_ids(task_type):
        """Получает список ID заданий указанного типа"""
        url = f"https://examinf.ru/api/tasks/ids/ege/{task_type}/"
        response = requests.get(url)
        return response.json()["result"]


    def get_task_stats(task_id):
        """Получает статистику для конкретного задания"""
        url = f"https://examinf.ru/api/task/{task_id}/additionalInfo/"
        response = requests.get(url)
        data = response.json()["result"]
        return data['usersSolvedCorrect'], data['usersSolvedWrong']


    def analyze_task_type(task_type):
        """Анализирует все задания указанного типа"""
        task_ids = get_task_ids(task_type)
        total_correct = 0
        total_wrong = 0

        for task_id in task_ids:
            try:
                correct, wrong = get_task_stats(task_id)
                total_correct += correct
                total_wrong += wrong
            except Exception as e:
                print(f"Ошибка при обработке задания {task_id}: {str(e)}")
                continue

        # Вычисляем процент правильных решений
        total_attempts = total_correct + total_wrong
        percent_correct = (total_correct / total_attempts * 100) if total_attempts > 0 else 0

        return {
            'totalUsersSolvedCorrect': total_correct,
            'totalUsersSolvedWrong': total_wrong,
            'percentCorrect': percent_correct
        }


    # Анализируем задания 18-го типа (можно изменить на нужный)
    stats = analyze_task_type(18)
    total_correct = stats['totalUsersSolvedCorrect']
    total_wrong = stats['totalUsersSolvedWrong']
    percent_correct = stats['percentCorrect']
    return total_correct, total_wrong, percent_correct

total_correct1, total_wrong1, percent_correct1 = get_ans()