import React from 'react';
import './GoalForm.css';

function GoalList({ goals, onDeleteGoal }) {
  return (
    <div className="form-container">
      {goals.length === 0 ? (
        <p className="no-goals-label">No Goals for Today</p>
      ) : (
        <div>
          {goals.map((goal, index) => (
            <button key={index} onClick={() => onDeleteGoal(goal)}>
              {goal}
            </button>
          ))}
        </div>
      )}
    </div>
  );
}

export default GoalList;