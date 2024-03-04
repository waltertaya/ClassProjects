const Routes = require('express');

const router = Routes();

let laptopParts = [
    {
        id: 1,
        name: 'Motherboard',
        number: 39,
        price: '$300',
        type: [
            'intel',
            'amd',
            'asus',
            'msi'
        ]
    },
    {
        id: 2,
        name: 'CPU',
        number: 40,
        price: '$1000',
        type: 'intel'
    },
    {
        id: 3,
        name: 'RAM',
        number: 50,
        price: '$200',
        type: 'intel',
        sizes: [
            '8GB',
            '16GB',
            '32GB'
        ]
    },
    {
        id: 4,
        name: 'GPU',
        number: 60,
        price: '$3000'
    },
    {
        id: 5,
        name: 'Storage',
        number: 70,
        price: '$100',
        type: [
            'HDD',
            'SSD'
        ],
        sizes: [
            '256GB',
            '512GB',
            '1TB'
        ]
    },
    {
        id: 6,
        name: 'PSU',
        number: 80,
        price: '$800'
    },
    {
        id: 7,
        name: 'Case',
        number: 90,
        price: '$90'
    }
];

router.use((req, res, next) => {
    if (req.session.user) {
        next();
    } else {
        res.send(401);
    }
});

router.get('/', (request, response) => {
    // console.log(request.query);
    // http://localhost:8000/api/v1/laptopComp?price=$100
    const { price } = request.query;
    if (price) {
        const filteredParts = laptopParts.filter(part => part.price === price);
        response.send(filteredParts);
    } else {
        response.send(laptopParts);
    }
});

router.get('/:id', (request, response) => {
    const id = request.params.id;
    response.send(laptopParts[id]);
});

router.post('/', (request, response) => {
    console.log(request.body);
    laptopParts.push(request.body);
    response.send(201);
});

module.exports = router;
