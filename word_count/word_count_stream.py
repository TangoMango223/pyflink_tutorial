from pyflink.datastream import StreamExecutionEnvironment
from pyflink.common.typeinfo import Types
from pyflink.datastream.functions import FlatMapFunction
from pyflink.common.watermark_strategy import WatermarkStrategy

class SplitWords(FlatMapFunction): # FlatMapFunction is a base class for flat map transformation
    def flat_map(self, value, collector): # collector emits results
        for word in value.split():
            collector.collect((word, 1)) # transforms to a tuple ("hello", 1) for example

def main():
    # Create the execution environment
    env = StreamExecutionEnvironment.get_execution_environment()
    env.set_parallelism(1)

    # Define the source: Simulating a stream of text
    text_stream = env.from_collection(
        collection=[
            "hello world",
            "apache flink streaming",
            "pyflink is awesome",
            "real-time processing",
        ],
        type_info=Types.STRING()
    )

    # Process the stream: Word count
    word_counts = (
        text_stream
        .flat_map(SplitWords(), output_type=Types.TUPLE([Types.STRING(), Types.INT()]))
        .key_by(lambda x: x[0])  # Group by the word
        .sum(1)  # Aggregate counts
    )

    # Define the sink: Print to console
    word_counts.print()

    # Execute the job
    env.execute("Word Count Streaming Job")

if __name__ == "__main__":
    main()
