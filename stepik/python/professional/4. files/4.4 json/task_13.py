import json

def find_best_pool():
    with open('pools.json', 'r', encoding='utf-8') as file:
        pools = json.load(file)
    
    best_pool = None
    best_length = 0
    best_width = 0
    
    for pool in pools:
        working_hours = pool.get('WorkingHoursSummer', {})
        monday_hours = working_hours.get('Понедельник')
        
        if not monday_hours:
            continue
            
        try:
            start_time, end_time = monday_hours.split('-')
            start_hour, start_minute = map(int, start_time.split(':'))
            end_hour, end_minute = map(int, end_time.split(':'))
            
            # Проверяем, что бассейн открыт с 10:00 до 12:00 включительно
            if start_hour > 10 or (start_hour == 10 and start_minute > 0):
                continue
                
            if end_hour < 12:
                continue
                
        except (ValueError, AttributeError):
            continue
        
        dimensions = pool.get('DimensionsSummer', {})
        length = dimensions.get('Length', 0)
        width = dimensions.get('Width', 0)
        
        # Выбираем бассейн с наибольшей длиной, при равенстве - с наибольшей шириной
        if length > best_length or (length == best_length and width > best_width):
            best_length = length
            best_width = width
            best_pool = pool
    
    if best_pool:
        print(f"{best_length}x{best_width}")
        print(best_pool['Address'])

find_best_pool()