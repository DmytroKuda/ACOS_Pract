import threading
import random
import time

# Функція для пошуку мінімуму в частині списку
def find_min_in_chunk(chunk, results, index):
    """
    chunk: частина списку для обробки
    results: спільний список для збереження результату
    index: позиція в списку results для цього потоку
    """
    if not chunk:
        return
    
    local_min = min(chunk)
    results[index] = local_min
    print(f"Потік {index} завершив пошук. Локальний мінімум: {local_min}")

def main():
    # 1. Створюємо великий масив випадкових чисел
    data_size = 1_000_000
    data = [random.randint(1, 10_000_000) for _ in range(data_size)]
    
    # Спеціально вставимо дуже маленьке число для перевірки
    secret_min = -999
    data[random.randint(0, data_size - 1)] = secret_min
    
    # 2. Визначаємо кількість потоків
    num_threads = 4
    chunk_size = data_size // num_threads
    threads = []
    
    # Список для зберігання мінімумів з кожного потоку
    min_results = [None] * num_threads

    start_time = time.time()

    # 3. Створюємо та запускаємо потоки
    for i in range(num_threads):
        start_idx = i * chunk_size
        # Останній потік забирає залишок, якщо ділення не націло
        end_idx = (i + 1) * chunk_size if i != num_threads - 1 else data_size
        
        chunk = data[start_idx:end_idx]
        
        t = threading.Thread(target=find_min_in_chunk, args=(chunk, min_results, i))
        threads.append(t)
        t.start()

    # 4. Очікуємо завершення всіх потоків (join)
    for t in threads:
        t.join()

    # 5. Знаходимо фінальний мінімум серед локальних результатів
    final_min = min(min_results)
    
    end_time = time.time()

    print("-" * 30)
    print(f"Пошук завершено за {end_time - start_time:.4f} сек.")
    print(f"Мінімуми по сегментах: {min_results}")
    print(f"Загальний мінімальний елемент: {final_min}")

if __name__ == "__main__":
    main()