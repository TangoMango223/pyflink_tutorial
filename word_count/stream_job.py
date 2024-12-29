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
        .flat_map(lambda line: line.split(), output_type=Types.STRING())
        .map(lambda word: (word, 1), output_type=Types.TUPLE([Types.STRING(), Types.INT()]))
        .key_by(lambda x: x[0])
        .reduce(lambda a, b: (a[0], a[1] + b[1]))
    )

    # Print results
    result.print()
    env.execute("Minikube WordCount Job")

if __name__ == "__main__":
    main()
    

# After you confirm the code runs:
"""
Use PyFlink to directly send the file to the Flink Cluster    

Step 1 - get name of the JobManager Pod:

>> kubectl get pods

Fill this out:
kubectl cp streaming_job.py <jobmanager-pod-name>:/opt/flink/

In my case, my job manager's pod name was: flink-jobmanager-78b9764ff-2vrlb

So, you fill it out as (make sure it's the FULL FILE NAME ON YOUR COMPUTER)

file name: /Users/christine/VSCode/pyflink_tutorial/pyflink_tutorial/word_count/stream_job.py


1. Push the file to the JobManager Pod - this has to be done when navigating to the flink folder in your laptop, and done thru terminal

>> kubectl cp /Users/christine/VSCode/pyflink_tutorial/pyflink_tutorial/word_count/stream_job.py flink-jobmanager-78b9764ff-2vrlb:/opt/flink/

2. Execute Flink Command:
>> kubectl exec -it flink-jobmanager-78b9764ff-2vrlb -- /opt/flink/bin/flink run /opt/flink/streaming_job.py

3. Check the results:
>> kubectl exec -it flink-jobmanager-78b9764ff-2vrlb -- /opt/flink/bin/flink list

"""
