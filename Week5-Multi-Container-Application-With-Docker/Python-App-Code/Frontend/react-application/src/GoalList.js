import React from 'react';
import './GoalForm.css';

function GoalList({ goals, onDeleteGoal }) {
  return (
    <div className="form-container">
      {goals.length === 0 ? (
        <p className="no-goals-label">No Goals for Today</p>
      ) : (
        <div>
          {goals.map((goal) => (
            <div key={goal.id}>
              <span>{goal.title}</span>
              <button onClick={() => onDeleteGoal(goal.id)}>Delete</button>
            </div>
          ))}
        </div>
      )}
    </div>
  );
}

export default GoalList;