import React, { useState } from 'react';

import './GoalForm.css';

function GoalForm() {
  const [goal, setGoal] = useState('');

  const handleGoalChange = (event) => {
    setGoal(event.target.value);
  };

  const handleSubmit = (event) => {
    event.preventDefault();
    console.log('Goal submitted:', goal);
    setGoal('');
  };

  return (
    <form className="form-container" onSubmit={handleSubmit}>
      <label htmlFor="goalInput">What do you want to do?</label>
      <input
        type="text"
        id="goalInput"
        value={goal}
        onChange={handleGoalChange}
        placeholder="What's on your mind?"
      />
      <button type="submit">Add Goal</button>
    </form>
  );
}

export default GoalForm;
