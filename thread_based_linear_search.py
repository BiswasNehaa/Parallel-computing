import threading 

def linear_search(arr, target, result):
    for index, element in enumerate(arr):
       if element== target:
           result['index']=index
           return
    result['index']= -1  # target not Found
    

data= [12,45,67,89,90,11]
target=89

# Dictionary to hold the output from the thread
search_result = {}

# 1. Create the thread
search_thread= threading.Thread(
    target=linear_search,
    args=(data, target, search_result)
)

# 2. Start the thread
search_thread.start()

# 3. Wait for the thread to finish executing
search_thread.join()

# Display results
if search_result.get('index') != -1:
    print(f"[Task 1] Target {target} found at index: {search_result['index']}")
else:
    print(f"[Task 1] Target {target} not found in array.")