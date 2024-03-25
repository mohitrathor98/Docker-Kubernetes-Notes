import React, { useState } from 'react';
import './GoalForm.css';

function GoalForm({ onAddGoal }) {
  const [goal, setGoal] = useState('');

  const handleGoalChange = (event) => {
    setGoal(event.target.value);
  };

  const handleSubmit = (event) => {
    event.preventDefault();
    if (goal.trim() !== '') {
      onAddGoal(goal);
      setGoal('');
    }
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
    </div>
  );
}

export default GoalForm;
