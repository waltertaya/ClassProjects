function laptop (name) {
    console.log(`You have successfully opened ${name} laptop`);
};

function HighOrderFunc (callback) {
    callback('Asus');
};

HighOrderFunc(laptop);
