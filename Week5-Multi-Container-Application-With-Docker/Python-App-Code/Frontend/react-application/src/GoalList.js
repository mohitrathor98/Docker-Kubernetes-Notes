import React from 'react';
import './GoalForm.css';

function GoalList({ goals, onClearGoal }) {
  return (
    <div className="form-container">
      {goals.length === 0 ? (
        <p className="no-goals-label">No Goals for Today</p>
      ) : (
        <div>
          {goals.map((goal, index) => (
            <button id="goal-buttons" key={index} onClick={() => onClearGoal(index)}>
              {goal}
            </button>
          ))}
        </div>
      )}
    </div>
  );
}

export default GoalList;
