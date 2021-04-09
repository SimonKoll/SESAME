import { TestBed } from '@angular/core/testing';

import { AppAuthGuardGuard } from './app-auth-guard.guard';

describe('AppAuthGuardGuard', () => {
  let guard: AppAuthGuardGuard;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    guard = TestBed.inject(AppAuthGuardGuard);
  });

  it('should be created', () => {
    expect(guard).toBeTruthy();
  });
});
