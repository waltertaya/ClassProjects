class Laptop {
    constructor (name) {
        this.name = name;
    };
    getName () {
        return this.name;
    };
    setName (name) {
        this.name = name;
    };
};

// module.exports = new Laptop('HP Pavilion 15');
module.exports = Laptop;