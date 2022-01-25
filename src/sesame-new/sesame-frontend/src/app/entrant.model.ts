export class Entrant {
    _id: number|undefined;
    name: string|undefined;
    timestamp: string|undefined;

    constructor(id:number, name:string, time:string){
      this._id=id
      this.name = name
      this.timestamp = time
    }

}


