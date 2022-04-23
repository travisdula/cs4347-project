export function Ticket(props: any) {
    const Fnum = props.flightNum
    const date = props.flightDate
    const Gnum = props.gateNum
    const Cid = props.customerID
    return (
        <div className="flex flex-col w-24">
            <div className="title text-xl font-bold text-left">{Fnum} {date}</div>
            <div className="flex flex-row flex-auto">
                <span className="text-left text-gray-700 font-semibold"> {Gnum} </span>
                <span className="text-right flex-grow text-gray-600"> {Cid} </span>
            </div>
        </div>
    )
}
