from pyflink.datastream import StreamExecutionEnvironment
from pyflink.common.typeinfo import Types

def main():
    env = StreamExecutionEnvironment.get_execution_environment()
    env.set_parallelism(1)

    # Simulated data source
    stream = env.from_collection(
        ["hello flink", "stream processing", "kubernetes deployment", "docker integration", "Christine", "Christine"]
    )

    # Word count logic
    result = (
        stream
        .flat_map(lambda line: line.split(), output_type=Types.STRING()) # split the line into words
        .map(lambda word: (word, 1), output_type=Types.TUPLE([Types.STRING(), Types.INT()])) # map each word to a tuple of (word, 1)
        .key_by(lambda x: x[0]) # equivalent to group by, group by keyword for counting, i.e. [("hello", 1), ("flink", 1), ("hello", 1), ("flink", 1), ("stream", 1)]
        # Result: [("hello", 2), ("flink", 2), ("stream", 1)]
        .reduce(lambda a, b: (a[0], a[1] + b[1])) # reduce by summing the counts
        # Since it's already grouped, this formula sums everything ups
    )

    # Print results
    result.print()
    env.execute("Minikube WordCount Job") # The name you put here will show up in the Flink UI as the job name

if __name__ == "__main__":
    main()