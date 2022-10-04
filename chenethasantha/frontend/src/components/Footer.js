import React from 'react';
import { Container, Row, Col } from 'react-bootstrap';

const year = new Date().getFullYear();

const Footer = () => {
  return (
    <footer>
      <Container>
        <Row>
          <Col className='text-center py-3'>
            Copyright &copy; <b>ChenethaSantha {`${year}`}</b>
            <br />
            <strong>
              <p className='small-text'>Developed by XtremeThinkerSolutions</p>
            </strong>
          </Col>
        </Row>
      </Container>
    </footer>
  );
};

export default Footer;
