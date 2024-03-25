import React, { useState } from 'react';
import GoalForm from './GoalForm';
import GoalList from './GoalList';

function GoalManager() {
  const [goalsList, setGoalsList] = useState([]);

  const handleAddGoal = (newGoal) => {
    setGoalsList([...goalsList, newGoal]);
  };

  const handleClearGoal = (index) => {
    const updatedGoalsList = goalsList.filter((_, i) => i !== index);
    setGoalsList(updatedGoalsList);
  };

  return (
    <div>
      <GoalForm onAddGoal={handleAddGoal} />
      <br></br>
      <GoalList goals={goalsList} onClearGoal={handleClearGoal} />
    </div>
  );
}

export default GoalManager;
