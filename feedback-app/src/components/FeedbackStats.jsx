import { useContext } from 'react';
import FeedbackContext from '../context/FeedbackContext';

function FeedbackStats() {
  const { feedback } = useContext(FeedbackContext);
  let ratingAverage =
    feedback.reduce((acc, curr) => {
      return acc + curr.rating;
    }, 0) / feedback.length;
  ratingAverage = ratingAverage.toFixed(1).replace(/[.,]0$/, '');
  return (
    <div className='feedback-stats'>
      <h4>No.of Reviews: {feedback.length}</h4>
      <h4>Avergae Rating: {isNaN(ratingAverage) ? 0 : ratingAverage}</h4>
    </div>
  );
}

export default FeedbackStats;
