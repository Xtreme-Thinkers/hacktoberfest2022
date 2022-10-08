import Card from '../components/shared/Card.jsx';
import { Link } from 'react-router-dom';
function AboutPage() {
  return (
    <Card>
      <div className='about'>
        <h1>About This Project</h1>
        <p>This is a react app to leave feedback for a product or services</p>
        <p>Version:1.0.0</p>
        <p>
          <Link to='/'>Back to Home</Link>
        </p>
      </div>
    </Card>
  );
}

export default AboutPage;
