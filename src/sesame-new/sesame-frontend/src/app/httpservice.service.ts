import { Injectable } from '@angular/core';
import { Observable, of, throwError } from 'rxjs';
import { HttpClient, HttpHeaders, HttpErrorResponse } from '@angular/common/http';
import { catchError, tap, map } from 'rxjs/operators';
import { Entrant } from './entrant.model';

const httpOptions = {
  headers: new HttpHeaders({'Content-Type': 'application/json'})
};
const apiUrl = 'http://localhost:3000';

@Injectable({
  providedIn: 'root'
})
export class HttpserviceService {

  constructor(private http: HttpClient) { }

  private handleError<T>(operation = 'operation', result?: T) {
    return (error: any): Observable<T> => {
      console.error(error);
      return of(result as T);
    };
  }


  getEntrants(): Observable<Entrant[]>  {
    return this.http.get<Entrant[]>(`${apiUrl}/get-entrant`);
}

  getEntrantById(id: string): Observable<Entrant> {
    const url = `${apiUrl}/${id}`;
    return this.http.get<Entrant>(url).pipe(
      tap(_ => console.log(`fetched entrants id=${id}`)),
      catchError(this.handleError<Entrant>(`getEntrantById id=${id}`))
    );
  }

  addEntrant(entrant: Entrant): Observable<Entrant> {
    return this.http.post<Entrant>(apiUrl, entrant, httpOptions).pipe(
      tap((e: Entrant) => console.log(`added entrants w/ id=${e._id}`)),
      catchError(this.handleError<Entrant>('addEntrant'))
    );
  }

  updateEntrant(id: string, entrant: Entrant): Observable<any> {
    const url = `${apiUrl}/${id}`;
    return this.http.put(url, entrant, httpOptions).pipe(
      tap(_ => console.log(`updated entrant id=${id}`)),
      catchError(this.handleError<any>('updateEntrant'))
    );
  }

  deleteEntrant(id: string): Observable<Entrant> {
    const url = `${apiUrl}/${id}`;
    return this.http.delete<Entrant>(url, httpOptions).pipe(
      tap(_ => console.log(`deleted entrant id=${id}`)),
      catchError(this.handleError<Entrant>('deleteEntrant'))
    );
  }
}
