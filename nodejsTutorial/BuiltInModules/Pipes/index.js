const fs = require('node:fs')
const zlib = require('node:zlib')

const gzip = zlib.createGzip()

const readableStream = fs.createReadStream('BuiltInModules/fsModule/file.txt', 
    {
        encoding: 'utf8',
        highWaterMark: 2
    }
)

readableStream.pipe(gzip).pipe(fs.createWriteStream('file.txt.gz'))

const WritableStream = fs.createWriteStream('file3.txt.gz')

readableStream.pipe(WritableStream)