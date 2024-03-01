# Streams recap

- A stream is a sequence of data i.e being moved from one point to another over time.
- EX: a stream of data being transferred from one file to another within the same computer.
- Work with data chunks instead of waiting for the entire data to be transferred.
- If you're transferring file contents from fileA to fileB, you don't wait for the entire fileA content to be saved in temporary memory before moving it into fileB.
- Instead, the content is transferred in chunks over time which prevents the unnecessary memory usage
- Stream is in fact a built-in node module that inherits from the event emitter class.
- Other modules internally use streams for their functioning.

## Types of Streams

1. Readable streams from which data can be read
2. Writable streams to which data can be written
3. Duplex streams that are both read and written
4. Transform streams that can modify or transform data as it is written or read

### Examples

a. Reading from a file as readable stream
b. Writing to a file as writable stream
c. Sockets as a duplex stream
d. File compression where you can write compressed data and read de-compressed data data to and from a file as a transform stream
