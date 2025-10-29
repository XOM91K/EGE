import datetime
class StudyPlanGenerator:
    def __init__(self):
        self.complexity_levels = {
            'легкая': {'total_hours': 4, 'days': 2},
            'средняя': {'total_hours': 8, 'days': 4},
            'сложная': {'total_hours': 12, 'days': 7}
        }
    def estimate_complexity(self, topic):
        """Оценка сложности темы на основе ключевых слов"""
        topic_lower = topic.lower()
        if any(word in topic_lower for word in ['введение', 'умножения', 'основы'
                                                , 'базовый', 'степень', 'свойства'
                                                , 'объекты', 'средний', 'средняя']):
            return 'лекая'
        elif any(word in topic_lower for word in ['продвинутый', 'алгоритм',
                                                  'сложной', 'сложная']):
            return 'сложная'
        else:
            return 'средняя'

    def generate_plan(self, topic, complexity=None):
        """ Генерация учебных планов """
        if not complexity:
            complexity = self.estimate_complexity(topic)
        config = self.complexity_levels[complexity]
        total_hours = config['total_hours']
        total_days = config['days']
        # Генерация структуры плана
        plan = {
            'topic': topic,
            'complexity': complexity,
            'total_hours': total_hours,
            'total_days': total_days,
            'daily_plan': self._generate_daily_schedule(topic, total_hours, total_days),
            'start_date': datetime.datetime.now().strftime('%Y-%m-%d'),
            'end_date': (datetime.datetime.now() + datetime.timedelta(days=total_days)).strftime('%Y-%m-%d')
        }
        return plan
    def _generate_daily_schedule(self, topic, total_hours, total_days):
        """Генерация ежедневного расписания"""
        hours_per_day = total_hours / total_days
        daily_plan = []
        stages = [
            "Теоретическое введение и основные понятия",
            "Практические основы и примеры",
            "Углубленное изучение ключевых аспектов",
            "Повторение и тестирование"
        ]
        current_date = datetime.datetime.now()
        # for day in range(total_days):
        #
        # todo: доделать и придумать как раскидывать темы по дням
        return daily_plan

    #todo: подумать над задачами, которые нужно прорешивать каждый день