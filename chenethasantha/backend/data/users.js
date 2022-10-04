import bcrypt from 'bcryptjs';

const users = [
  {
    name: 'Admin User',
    email: 'admin@gmail.com',
    password: bcrypt.hashSync('admin212', 10),
    isAdmin: true,
  },
  {
    name: 'mounika',
    email: 'mounikaupendram2@gmail.com',
    password: bcrypt.hashSync('mounika', 10),
    isAdmin: false,
  },
  {
    name: 'manjunath',
    email: 'manjunatha16.512@gmail.com',
    password: bcrypt.hashSync('manjunath', 10),
    isAdmin: false,
  },
];

export default users;
