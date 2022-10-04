import React, { useState } from 'react';
import { Row, Form, Button, FormControl, Col } from 'react-bootstrap';
import { useNavigate } from 'react-router-dom';

const SearchBox = () => {
  const history = useNavigate();
  const [keyword, setKeyword] = useState('');

  const submitHandler = (e) => {
    e.preventDefault();
    if (keyword.trim()) {
      history(`/search/${keyword}`);
    } else {
      history('/');
    }
  };

  return (
    <Form onSubmit={submitHandler} inline>
      <Row>
        <Col>
          <FormControl
            type='text'
            name='q'
            onChange={(e) => setKeyword(e.target.value)}
            placeholder='Search'
            className='mr-sm-2 ml-sm-1 curved-box'
          ></FormControl>
        </Col>
        <Col>
          <Button
            type='submit'
            variant='outline-success'
            className='p-1 m-1 curved-button'
          >
            Search
          </Button>
        </Col>
      </Row>
    </Form>
  );
};

export default SearchBox;
