const Routes = require('express');

const router = Routes();

let laptops = [
    {
        name: 'Asus',
        number: 39,
        price: '$300'
    },
    {
        name: 'Dell',
        number: 40,
        price: '$1000'
    },
    {
        name: 'HP',
        number: 50,
        price: '$200'
    },
    {
        name: 'Lenovo',
        number: 60,
        price: '$3000'
    },
    {
        name: 'Acer',
        number: 70,
        price: '$100'
    },
    {
        name: 'Apple',
        number: 80,
        price: '$200'
    },
    {
        name: 'MSI',
        number: 90,
        price: '$3000'
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
    // cookies setups
    // response.cookie('visited', true, {
    //     maxAge: 1000 * 60 * 60 * 24,
    //     httpOnly: true
    // });
    response.send(laptops);
});

router.get('/:id', (request, response) => {
    // Check if use send cookies
    // console.log(request.cookies);
    const id = request.params.id;
    response.send(laptops[id]);
});

router.post('/', (request, response) => {
    console.log(request.body);
    laptops.push(request.body);
    response.send(201);
});

router.get('/shopping/cart', (request, response) => {
    const { cart } = request.session;
    if (!cart) {
        response.send('You have no cart!!!!');
    } else {
        response.send(cart);
    }
});

router.post('/shopping/cart/item', (request, response) => {
    const { product, quantity } = request.body;
    const products = { product, quantity };
    const { cart } = request.session;
    if (cart) {
        request.session.cart.items.push(products);
    } else {
        request.session.cart = {
            items: [products]
        };
    }
    response.send(201);
});

module.exports = router;