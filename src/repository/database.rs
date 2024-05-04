use std::fmt::Error;
use chrono::prelude::*;
use diesel::prelude::*;
use diesel::r2d2::{self, ConnectionManager};
use dotenv::dotenv;

use crate::models::task::Task;
use crate::repository::schema::tasks::dsl::*;

type DBPool = r2d2::Pool<ConnectionManager<PgConnection>>;

pub struct Database {
    pool: DBPool,
}

impl Database {

    pub fn new() -> Self {
        dotenv().ok();
        let database_url = std::env::var("DATABASE_URL").expect("DATABASE_URL must be set");
        let manager = ConnectionManager::<PgConnection>::new(database_url);
        let pool: DBPool = r2d2::Pool::builder()
            .build(manager)
            .expect("Failed to create pool.");
        Database { pool }
    }

    pub fn get_tasks(&self) -> Vec<Task> {
        tasks
            .load::<Task>(&mut self.pool.get().unwrap())
            .expect("Error loading all tasks")
    }

    pub fn create_task(&self, task: Task) -> Result<Task, Error> {
        let task = Task {
            id: uuid::Uuid::new_v4().to_string(),
            created_at: Some(Utc::now().naive_utc()),
            updated_at: Some(Utc::now().naive_utc()),
            ..task
        };
        diesel::insert_into(tasks)
            .values(&task)
            .execute(&mut self.pool.get().unwrap())
            .expect("Error creating new task");
        Ok(task)
    }

    pub fn get_task_by_id(&self, task_id: &str) -> Option<Task> {
        let task = tasks
            .find(task_id)
            .get_result::<Task>(&mut self.pool.get().unwrap())
            .expect("Error loading task by id");
        Some(task)
    }

    pub fn delete_task_by_id(&self, task_id: &str) -> Option<usize> {
        let count = diesel::delete(tasks.find(task_id))
            .execute(&mut self.pool.get().unwrap())
            .expect("Error deleting task by id");
        Some(count)
    }


    pub fn update_task_by_id(&self, task_id: &str, mut task: Task) -> Option<Task> {
        task.updated_at = Some(Utc::now().naive_utc());
        let task = diesel::update(tasks.find(task_id))
            .set(&task)
            .get_result::<Task>(&mut self.pool.get().unwrap())
            .expect("Error updating task by id");
        Some(task)
    }
}