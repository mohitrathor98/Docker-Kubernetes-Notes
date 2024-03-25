import React, { useState } from 'react';
import './GoalForm.css';

function GoalForm() {
  const [goal, setGoal] = useState('');
  const [goalsList, setGoalsList] = useState([]);
  
  const handleGoalChange = (event) => {
    setGoal(event.target.value);
  };

  const handleSubmit = (event) => {
    event.preventDefault();
    if (goal.trim() !== '') {
      setGoalsList([...goalsList, goal]);
      setGoal('');
    }
  };

  const handleClearGoal = (index) => {
    const updatedGoalsList = goalsList.filter((_, i) => i !== index);
    setGoalsList(updatedGoalsList);
  };

  return (
    <div className="form-container">
      <form onSubmit={handleSubmit}>
        <label htmlFor="goalInput">Goal Tracker</label>
        <input
          type="text"
          id="goalInput"
          value={goal}
          onChange={handleGoalChange}
          placeholder="Enter your goal"
        />
        <button type="submit">What do you want to do?</button>
      </form>
    
      {goalsList.length === 0 ? (
        <p className="no-goals-label">No Goals for Today</p>
      ) : (
        <div>
          {goalsList.map((goal, index) => (
            <button id="goal-buttons" key={index} onClick={() => handleClearGoal(index)}>
              {goal}
            </button>
          ))}
        </div>
      )}
    </div>
  );
}

export default GoalForm;
