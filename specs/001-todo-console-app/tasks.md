---
description: "Task list for Todo In-Memory Python Console Application"
---

# Tasks: Todo In-Memory Python Console Application

**Input**: Design documents from `/specs/001-todo-console-app/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/

**Tests**: The examples below include test tasks. Tests are OPTIONAL - only include them if explicitly requested in the feature specification.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Single project**: `src/`, `tests/` at repository root
- Paths shown below assume single project - adjust based on plan.md structure

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [X] T001 Create project structure per implementation plan in src/todo_app/
- [X] T002 Create src/todo_app/__init__.py
- [X] T003 [P] Create src/todo_app/models/__init__.py
- [X] T004 [P] Create src/todo_app/services/__init__.py
- [X] T005 [P] Create src/todo_app/cli/__init__.py
- [X] T006 [P] Create src/todo_app/utils/__init__.py
- [X] T007 [P] Create tests/__init__.py
- [X] T008 [P] Create tests/unit/__init__.py
- [X] T009 [P] Create tests/integration/__init__.py

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [X] T010 [P] Create Todo model in src/todo_app/models/todo.py
- [X] T011 [P] Create in-memory store in src/todo_app/services/store.py
- [X] T012 Create main application entry point in src/todo_app/cli/app.py
- [X] T013 Create menu interface in src/todo_app/cli/menu.py
- [X] T014 Create validators utility in src/todo_app/utils/validators.py
- [X] T015 Create main.py entry point at repository root

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Add Todo Item (Priority: P1) 🎯 MVP

**Goal**: Enable users to add new todo items with a description via the command-line interface, creating a new todo item with a unique identifier and pending status

**Independent Test**: Can be fully tested by running the application, selecting the add option, entering a task description, and verifying that the task appears in the list with a unique ID and pending status

### Tests for User Story 1 (OPTIONAL - only if tests requested) ⚠️

> **NOTE: Write these tests FIRST, ensure they FAIL before implementation**

- [ ] T016 [P] [US1] Unit test for Todo model in tests/unit/test_todo_model.py
- [ ] T017 [P] [US1] Unit test for store add functionality in tests/unit/test_store.py
- [ ] T018 [P] [US1] Integration test for add todo flow in tests/integration/test_add_todo.py

### Implementation for User Story 1

- [X] T019 [P] [US1] Implement Todo model with id, title, completed fields in src/todo_app/models/todo.py
- [X] T020 [US1] Implement add_todo method in src/todo_app/services/store.py
- [X] T021 [US1] Implement input validation for todo title in src/todo_app/utils/validators.py
- [X] T022 [US1] Create TodoService with add functionality in src/todo_app/services/todo_service.py
- [X] T023 [US1] Implement add todo menu option in src/todo_app/cli/menu.py
- [X] T024 [US1] Integrate add todo functionality in src/todo_app/cli/app.py

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently

---

## Phase 4: User Story 2 - View All Todo Items (Priority: P1)

**Goal**: Enable users to see all their todo items displayed in a readable format showing ID, description, and completion status

**Independent Test**: Can be fully tested by adding some todo items, then viewing the list and confirming all items are displayed with their correct details

### Tests for User Story 2 (OPTIONAL - only if tests requested) ⚠️

- [ ] T025 [P] [US2] Unit test for store get_all functionality in tests/unit/test_store.py
- [ ] T026 [P] [US2] Integration test for view todos flow in tests/integration/test_view_todos.py

### Implementation for User Story 2

- [X] T027 [P] [US2] Implement get_all_todos method in src/todo_app/services/store.py
- [X] T028 [US2] Create TodoService method for getting all todos in src/todo_app/services/todo_service.py
- [X] T029 [US2] Implement view todos menu option in src/todo_app/cli/menu.py
- [X] T030 [US2] Integrate view todos functionality in src/todo_app/cli/app.py

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently

---

## Phase 5: User Story 3 - Mark Todo as Completed (Priority: P2)

**Goal**: Enable users to mark a specific todo item as completed to track their progress

**Independent Test**: Can be fully tested by adding a todo item, marking it as completed, and verifying that its status changes to completed when viewed

### Tests for User Story 3 (OPTIONAL - only if tests requested) ⚠️

- [ ] T031 [P] [US3] Unit test for store update functionality in tests/unit/test_store.py
- [ ] T032 [P] [US3] Integration test for mark complete flow in tests/integration/test_mark_complete.py

### Implementation for User Story 3

- [X] T033 [P] [US3] Implement update_todo method in src/todo_app/services/store.py
- [X] T034 [US3] Create TodoService method for marking complete in src/todo_app/services/todo_service.py
- [X] T035 [US3] Implement mark complete menu option in src/todo_app/cli/menu.py
- [X] T036 [US3] Integrate mark complete functionality in src/todo_app/cli/app.py

**Checkpoint**: All user stories should now be independently functional

---

## Phase 6: User Story 4 - Update Todo Item (Priority: P2)

**Goal**: Enable users to modify the description of an existing todo item to correct or refine their task details

**Independent Test**: Can be fully tested by adding a todo item, updating its description, and verifying that the change is reflected when viewing the list

### Tests for User Story 4 (OPTIONAL - only if tests requested) ⚠️

- [ ] T037 [P] [US4] Unit test for update todo functionality in tests/unit/test_todo_service.py
- [ ] T038 [P] [US4] Integration test for update todo flow in tests/integration/test_update_todo.py

### Implementation for User Story 4

- [X] T039 [P] [US4] Enhance update_todo method in src/todo_app/services/store.py
- [X] T040 [US4] Create TodoService method for updating todo description in src/todo_app/services/todo_service.py
- [X] T041 [US4] Implement update todo menu option in src/todo_app/cli/menu.py
- [X] T042 [US4] Integrate update todo functionality in src/todo_app/cli/app.py

---

## Phase 7: User Story 5 - Delete Todo Item (Priority: P3)

**Goal**: Enable users to remove a todo item that is no longer needed or relevant

**Independent Test**: Can be fully tested by adding a todo item, deleting it, and verifying that it no longer appears in the list

### Tests for User Story 5 (OPTIONAL - only if tests requested) ⚠️

- [ ] T043 [P] [US5] Unit test for store delete functionality in tests/unit/test_store.py
- [ ] T044 [P] [US5] Integration test for delete todo flow in tests/integration/test_delete_todo.py

### Implementation for User Story 5

- [X] T045 [P] [US5] Implement delete_todo method in src/todo_app/services/store.py
- [X] T046 [US5] Create TodoService method for deleting todo in src/todo_app/services/todo_service.py
- [X] T047 [US5] Implement delete todo menu option in src/todo_app/cli/menu.py
- [X] T048 [US5] Integrate delete todo functionality in src/todo_app/cli/app.py

---

## Phase 8: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [X] T049 [P] Implement error handling and user feedback across all operations in src/todo_app/cli/app.py
- [X] T050 [P] Add graceful exit functionality in src/todo_app/cli/app.py
- [X] T051 [P] Add input validation across all user inputs in src/todo_app/utils/validators.py
- [X] T052 [P] Implement full menu navigation in src/todo_app/cli/menu.py
- [X] T053 [P] Create comprehensive tests in tests/unit/test_todo_service.py
- [X] T054 [P] Add edge case handling for invalid IDs and inputs in src/todo_app/utils/validators.py
- [X] T055 Run quickstart.md validation

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3+)**: All depend on Foundational phase completion
  - User stories can then proceed in parallel (if staffed)
  - Or sequentially in priority order (P1 → P2 → P3)
- **Polish (Final Phase)**: Depends on all desired user stories being complete

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 2 (P2)**: Can start after Foundational (Phase 2) - May integrate with US1 but should be independently testable
- **User Story 3 (P3)**: Can start after Foundational (Phase 2) - May integrate with US1/US2 but should be independently testable
- **User Story 4 (P4)**: Can start after Foundational (Phase 2) - May integrate with US1/US2/US3 but should be independently testable
- **User Story 5 (P5)**: Can start after Foundational (Phase 2) - May integrate with US1/US2/US3/US4 but should be independently testable

### Within Each User Story

- Tests (if included) MUST be written and FAIL before implementation
- Models before services
- Services before endpoints
- Core implementation before integration
- Story complete before moving to next priority

### Parallel Opportunities

- All Setup tasks marked [P] can run in parallel
- All Foundational tasks marked [P] can run in parallel (within Phase 2)
- Once Foundational phase completes, all user stories can start in parallel (if team capacity allows)
- All tests for a user story marked [P] can run in parallel
- Models within a story marked [P] can run in parallel
- Different user stories can be worked on in parallel by different team members

---

## Parallel Example: User Story 1

```bash
# Launch all tests for User Story 1 together (if tests requested):
Task: "Unit test for Todo model in tests/unit/test_todo_model.py"
Task: "Unit test for store add functionality in tests/unit/test_store.py"
Task: "Integration test for add todo flow in tests/integration/test_add_todo.py"

# Launch all models for User Story 1 together:
Task: "Implement Todo model with id, title, completed fields in src/todo_app/models/todo.py"
Task: "Implement add_todo method in src/todo_app/services/store.py"
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational (CRITICAL - blocks all stories)
3. Complete Phase 3: User Story 1
4. **STOP and VALIDATE**: Test User Story 1 independently
5. Deploy/demo if ready

### Incremental Delivery

1. Complete Setup + Foundational → Foundation ready
2. Add User Story 1 → Test independently → Deploy/Demo (MVP!)
3. Add User Story 2 → Test independently → Deploy/Demo
4. Add User Story 3 → Test independently → Deploy/Demo
5. Each story adds value without breaking previous stories

### Parallel Team Strategy

With multiple developers:

1. Team completes Setup + Foundational together
2. Once Foundational is done:
   - Developer A: User Story 1
   - Developer B: User Story 2
   - Developer C: User Story 3
3. Stories complete and integrate independently

---

## Notes

- [P] tasks = different files, no dependencies
- [Story] label maps task to specific user story for traceability
- Each user story should be independently completable and testable
- Verify tests fail before implementing
- Commit after each task or logical group
- Stop at any checkpoint to validate story independently
- Avoid: vague tasks, same file conflicts, cross-story dependencies that break independence