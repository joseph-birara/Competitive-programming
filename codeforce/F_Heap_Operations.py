import heapq


def main():
    num_operations = int(input())

    output = []
    heap = []
    for i in range(num_operations):
        record = list(input().split())

        if record[0] == 'insert':
            heapq.heappush(heap, int(record[1]))
            output.append(record)

        elif record[0] == 'removeMin':
            if not heap:
                output.append(['insert', '1'])
                heapq.heappush(heap, 1)
            heapq.heappop(heap)
            output.append(record)

        else:
            x = int(record[1])

            while heap and heap[0] < x:
                heapq.heappop(heap)
                output.append(['removeMin'])

            if not heap or heap[0] > x:
                heapq.heappush(heap, x)
                output.append(['insert',  str(x)])

            output.append(record)

    print(len(output))
    for line in output:
        print(' '.join(line))


main()
